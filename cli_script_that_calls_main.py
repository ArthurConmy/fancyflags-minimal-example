import fancyflags as ff
import absl.app # ff requires us to use absl.app to run main
from true_main import main as true_main_function

_MY_DIFFERENT_DICT = ff.DEFINE_dict(
    "my_different_dict",
    int_arg=ff.Integer(int(1e7)),
    float_arg=ff.Float(0.7),
    str_arg=ff.String("my_different_string"),
)

def main(argv): # Need to pass argv even though it's unused
    my_different_dict = _MY_DIFFERENT_DICT.value  # `.value` returns a dict
    print(f"{my_different_dict=}")

    return true_main_function(argv, my_dict=my_different_dict)

if __name__ == "__main__":
    absl.app.run(main)
