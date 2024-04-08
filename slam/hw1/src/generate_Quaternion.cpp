#include <iostream>

#include <fstream>
#include <sstream>
#include <vector>
#include <tuple>
#include <math.h>
#include <Eigen/Core>

// std::vector<Eigen::Matrix<double, 3, 3>> caculate__(std::vector<std::vector<double>> data)
// {
//     std::vector<Eigen::Matrix<double, 3, 3>> result;
//     for (int i = 0; i < 13; i++)
//     {
//         Eigen::Matrix<double, 3, 3> matrix;
//         matrix << cos(data[2][i]), -sin(data[2][i]), 0, sin(data[2][i]), cos(data[2][i]), 0, 0, 0, 0;
//         result.push_back(matrix);
//     }
//     return result;
// }
struct Quaternion
{
    double w, x, y, z;
};

Quaternion ToQuaternion(double yaw, double pitch, double roll) // yaw (Z), pitch (Y), roll (X)
{
    // Abbreviations for the various angular functions
    double cy = cos(yaw * 0.5);
    double sy = sin(yaw * 0.5);
    double cp = cos(pitch * 0.5);
    double sp = sin(pitch * 0.5);
    double cr = cos(roll * 0.5);
    double sr = sin(roll * 0.5);

    Quaternion q;
    q.w = cy * cp * cr + sy * sp * sr;
    q.x = cy * cp * sr - sy * sp * cr;
    q.y = sy * cp * sr + cy * sp * cr;
    q.z = sy * cp * cr - cy * sp * sr;

    return q;
}
int main()

{
    std::string file_path = "../source/hw1_data.txt";

    std::ifstream in(file_path);

    std::string line;
    std::vector<std::vector<double>> data;
    while (std::getline(in, line))
    {
        std::vector<double> row;
        std::istringstream iss(line);
        double value;
        while (iss >> value)
        {
            row.push_back(value);
            std::cout << value << std::endl;
        }
        data.push_back(row);
    }

    std::vector<Quaternion> result;

    for (int i = 0; i < 13; i++)
    {
        double yaw = data[2][i];
        std::cout << yaw << std::endl;
        double pitch = 0;
        double roll = 0;
        Quaternion q = ToQuaternion(yaw, pitch, roll);
        result.push_back(q);
    }
    for (auto item : result)
    {
        std::cout << item.x << " " << item.y << " " << item.z << " " << item.w << std::endl;
    }

    std::ofstream out("../source/hw1_result_evo.txt");
    std::tuple<double, double, double> result_;
    for (int i = 0; i < 12; i++)
    {
        if (i == 0)
        {
            double x = std::cos(data[2][i]) * 1 - std::sin(data[2][i]) * 0 + data[0][i] * 0;
            double y = std::sin(data[2][i]) * 1 + std::cos(data[2][i]) * 0 + data[1][i] * 0;
            double theta = 0;
            result_ = std::make_tuple(x, y, theta);
        }
        else
        {
            double x = std::cos(data[2][i]) * std::get<0>(result_) - std::sin(data[2][i]) * std::get<1>(result_) + data[0][i] * std::get<2>(result_);
            double y = std::sin(data[2][i]) * std::get<0>(result_) + std::cos(data[2][i]) * std::get<1>(result_) + data[1][i] * std::get<2>(result_);
            double theta = std::get<2>(result_);
            result_ = std::make_tuple(x, y, theta);
        }
        out << i + 1 << " " << std::get<0>(result_) << " " << std::get<1>(result_) << " " << 0 << " " << result[i].x << " " << result[i].y << " " << result[i].z << " " << result[i].w << std::endl;
    }
    return 0;
}