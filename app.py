from absl import app
from absl import flags


"""
1 -- add WORKSPACE file
2 -- add BUILD file with your build rules
3 -- use bazel to build --> bazel build: app
4 -- use bazel to execute the generated executable --> bazel-bin/app --name=Daenerys --num=10
"""
flags.DEFINE_string('name', None, 'Username')
flags.DEFINE_integer('num', 1, 'number of times')

# Must be provided by user
flags.mark_flag_as_required('name')

# Entry func of program
def main(argv):
    del argv

    for i in range(0, flags.FLAGS.num):
        print(flags.FLAGS.name)

# Entry point of exec
if __name__ == '__main__':
    app.run(main)