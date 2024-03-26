For the first build,
conda activate mlenv

(Otherwise ninja won't be found)

Then, in cpp_interface
./build_test_torch_model.sh

Then, in build (where model_cpu must be copied!)

./test_torch_model model_cpu.ptc

or if you don't copy the file

./test_torch_model ../cpp_interface/model_cpu.ptc


In addition, to handle memory issues, one can use
ulimit -s unlimited
