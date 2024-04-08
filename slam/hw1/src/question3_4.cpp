#include <stdio.h>
#include <iostream>
#include <g2o/core/block_solver.h>
#include <g2o/solvers/eigen/linear_solver_eigen.h>
#include <g2o/core/optimization_algorithm_levenberg.h>
#include <g2o/types/slam2d/types_slam2d.h>
#include <Eigen/Core>

typedef struct
{
    int s, e;
    Eigen::Vector2d pose;
} Edge;
typedef g2o::BlockSolver<g2o::BlockSolverTraits<2, 2>> SlamBlockSolver;
typedef g2o::LinearSolverEigen<SlamBlockSolver::PoseMatrixType> SlamLinearSolver;

int main(int argc, const char *argv[])
{

    std::vector<Edge> edgeData = {
        {0, 1, {-0.10536000000000001, 0.446787}},
        {1, 2, {-0.370425, 0.40479899999999996}},
        {2, 3, {-0.4316354, 0.144119}},
        {3, 4, {-0.48387959999999997, -0.0754419999999999}},
        {4, 5, {-0.442767, -0.368599}},
        {5, 6, {-0.16589500000000001, -0.5429094600000001}},
        {6, 7, {0.12096200000000001, -0.48557654}},
        {7, 8, {0.394949, -0.398218}},
        {8, 9, {0.47664409, -0.12493299999999996}},
        {9, 10, {0.44859191, 0.10255700000000001}},
        {10, 11, {0.35503199999999996, 0.292405}},
        {11, 12, {0.19373300000000004, 0.46358999999999995}},
        {12, 0, {0.0, 0.0}},
        // {11, 12, {0.0, 0.0}}
    };

    std::unique_ptr<SlamLinearSolver> linearSolver = std::make_unique<SlamLinearSolver>();
    linearSolver->setBlockOrdering(false);
    g2o::OptimizationAlgorithmLevenberg *solver = new g2o::OptimizationAlgorithmLevenberg(std::make_unique<SlamBlockSolver>(std::move(linearSolver)));

    g2o::SparseOptimizer optimizer;
    optimizer.setAlgorithm(solver);
    optimizer.setVerbose(true);

    auto maxEdge = std::max_element(edgeData.begin(), edgeData.end(), [](const Edge &a, const Edge &b)
                                    { return std::max(a.e, a.s) < std::max(b.e, b.s); });
    int maxIndex = std::max(maxEdge->s, maxEdge->e);

    for (int i = 0; i < maxIndex + 1; i++)
    {
        g2o::VertexPointXY *v = new g2o::VertexPointXY();
        v->setId(i);
        v->setEstimate(g2o::Vector2());
        if (i == 0)
        {
            // v->setEstimate(edgeData[0].pose);
            v->setEstimate(Eigen::Vector2d(1.0, 0.0));
            v->setFixed(true);
        }
        optimizer.addVertex(v);
    }

    for (const auto &pData : edgeData)
    {
        g2o::EdgePointXY *edge = new g2o::EdgePointXY();
        edge->setVertex(0, optimizer.vertex(pData.s));
        edge->setVertex(1, optimizer.vertex(pData.e));
        edge->setInformation(Eigen::Matrix<double, 2, 2>::Identity()); // 信息矩阵表示2维上侧重哪一维，xy是一样重要的，所以就是单位矩阵，但是在6维的位姿中，有可能更侧重优化旋转或者位移，就需要设置信息矩阵
        edge->setMeasurement(pData.pose);
        optimizer.addEdge(edge);
    }

    optimizer.initializeOptimization();
    optimizer.optimize(500);
    std::ofstream out("../source/hello_g2o.txt");
    for (int i = 0; i < maxIndex + 1; i++)
    {
        g2o::VertexPointXY *vertex = dynamic_cast<g2o::VertexPointXY *>(optimizer.vertex(i));
        g2o::Vector2 pose = vertex->estimate();
        out << pose[0] << " " << pose[1] << std::endl;
    }
    return 0;
}
