cmake_minimum_required(VERSION 3.16 )
project(cxxTorch CXX)

set(CMAKE_CXX_FLAGS "-std=c++11")
# set(CMAKE_BUILD_TYPE Debug)
SET(CMAKE_BUILD_TYPE "Debug")
# SET(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g2 -ggdb")
# SET(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

# 查找CUDA
find_package(CUDA REQUIRED)
# message("-- Found CUDA version ${CUDA_VERSION}: ")
# include_directories(${CUDA_INCLUDE_DIRS})

# link_directories(/usr/local/cuda-12.1/lib64)
# link_directories(/usr/local/cuda-12.1/lib64/stubs)
# link_directories(/usr/local/cuda-12.1/targets/x86_64-linux/lib/)
# find_package(Torch REQUIRED)

find_package(OpenCV 4.5.0 REQUIRED)



# include_directories(${TORCH_INCLUDE_DIRS})
include_directories(${OpenCV_INCLUDE_DIRS})


#查找engine
set(ENGINE_INCLUDE_DIRS "/usr/include/eigen3")

include_directories(${ENGINE_INCLUDE_DIRS})
#查找 CERES
find_package(Ceres REQUIRED)
include_directories(${CERES_INCLUDE_DIRS})

# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -pthread -Wno-format -fpermissive -B -fopenacc     ")


#添加可执行文件
add_executable(main ./src/hw1_.cpp)

#添加链接库
# message("CERES_LIBS =  ${CERES_LIBRARIES}")
target_link_libraries(main cudart g2o_core g2o_stuff g2o_types_slam2d g2o_opengl_helper   ${OpenCV_LIBS} ${CERES_LIBRARIES})#

#设置编译选项
target_compile_options(main PRIVATE -std=c++17 -g -pthread -Wno-format -fpermissive -B -fopenacc   -lcudart -lcuda)

# target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS} "${TORCH_LIBRARIES}" )

set_property(TARGET main PROPERTY CXX_STANDARD 17)



# 需要找到Libtorch
# set(CMAKE_PREFIX_PATH "/opt/miniconda3/envs/mmdt/lib/python3.8/site-packages/torch/share/cmake")
# target_include_directories(${PROJECT_NAME} PRIVATE "${TORCH_INCLUDE_DIRS}")
# target_link_libraries(${PROJECT_NAME} ${TORCH_LIBRARIES} ${TORCH_LIBRARIES} )
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS} -std=c++17")

# target_link_libraries(${PROJECT_NAME} -lopencv_dnn -lopencv_gapi -lopencv_highgui -lopencv_ml -lopencv_objdetect -lopencv_photo -lopencv_stitching -lopencv_video -lopencv_calib3d -lopencv_features2d -lopencv_flann -lopencv_videoio -lopencv_imgcodecs -lopencv_imgproc -lopencv_core)