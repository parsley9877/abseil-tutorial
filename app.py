from absl import app
from absl import flags


"""
1 -- add WORKSPACE file
2 -- add BUILD file with your build rules
3 -- use bazel to build --> bazel build: app
4 -- use bazel to execute the generated executable --> bazel-bin/app --name=Daenerys --num=10

Note -- use 'bazel-bin/app --help' for help on flags
Note -- use 'bazel-bin/app --flagfile=flags.cfg' for inputing flags from a file
"""
flags.DEFINE_string('name', None, 'Username')
flags.DEFINE_integer('num', 1, 'number of times')

# Must be provided by user
flags.mark_flag_as_required('name')

# flag validators
def num_checker(number):
    return number % 3 == 0

# assigning flag validator
flags.register_validator('num', checker=num_checker, message='Number of times must be divisable by 3')

# Entry func of program
def main(argv):
    # delete argv if you are not going to use it, or you will get error
    del argv

    for i in range(0, flags.FLAGS.num):
        print(flags.FLAGS.name)

# Entry point of exec
if __name__ == '__main__':
    app.run(main)