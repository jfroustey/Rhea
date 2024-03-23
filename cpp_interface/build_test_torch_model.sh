~/miniconda3/envs/mlenv/bin/cmake --no-warn-unused-cli -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=TRUE -DCMAKE_BUILD_TYPE:STRING=Debug -DCMAKE_C_COMPILER:FILEPATH=/usr/bin/gcc -DCMAKE_CXX_COMPILER:FILEPATH=/usr/bin/g++ -S~/Documents/Rhea/cpp_interface -B~/Documents/Rhea/build -G Ninja

~/miniconda3/envs/mlenv/bin/cmake --build ~/Documents/Rhea/build --config Debug --target all --
