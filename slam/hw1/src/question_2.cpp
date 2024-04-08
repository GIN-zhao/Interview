#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <tuple>
#include <math.h>
std::tuple<double, double, double> caculate_(std::vector<std::vector<double>> data)
{
    std::ofstream out("../source/hw1_result.txt");

    std::tuple<double, double, double> result;
    int n = 12;
    for (int i = 0; i < n; i++)
    {
        if (i == 0)
        {
            double x = std::cos(data[2][i]) * 1 - std::sin(data[2][i]) * 0 + data[0][i] * 0;
            double y = std::sin(data[2][i]) * 1 + std::cos(data[2][i]) * 0 + data[1][i] * 0;
            double theta = 0;
            result = std::make_tuple(x, y, theta);
        }
        else
        {
            double x = std::cos(data[2][i]) * std::get<0>(result) - std::sin(data[2][i]) * std::get<1>(result) + data[0][i] * std::get<2>(result);
            double y = std::sin(data[2][i]) * std::get<0>(result) + std::cos(data[2][i]) * std::get<1>(result) + data[1][i] * std::get<2>(result);
            double theta = std::get<2>(result);
            result = std::make_tuple(x, y, theta);
        }
        // std::cout << "x= " << std::get<0>(result) << " y= " << std::get<1>(result) << std::endl;
        out << std::get<0>(result) << " " << std::get<1>(result) << std::endl;
        // std::cout << std::get<0>(result) << " " << std::get<1>(result) << " " << std::get<2>(result) << std::endl;
    }
    return result;
}
int main()

{
    std::vector<std::vector<double>> data;

    const std::string input = "../source/hw1_data.txt";

    std::ifstream in(input);

    std::string line;
    while (std::getline(in, line))
    {
        std::vector<double> row;
        std::istringstream iss(line);
        double value;
        while (iss >> value)
        {
            row.push_back(value);
        }
        data.push_back(row);
    }
    auto outcome = caculate_(data);

    return 0;
}