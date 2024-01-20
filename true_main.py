import fancyflags as ff
import absl.app # ff requires us to use absl.app to run main

_MY_DICT = ff.DEFINE_dict(
    "my_dict",
    int_arg=ff.Integer(int(1e6)),
    float_arg=ff.Float(0.6),
    str_arg=ff.String("my_string"),
)

def main(
    argv, # Need to pass argv even though it's unused
    my_dict: dict | None = None,
):
    my_dict = my_dict or _MY_DICT.value  # `.value` returns a dict
    print(f"{my_dict=}")

if __name__ == "__main__":
    absl.app.run(main)
