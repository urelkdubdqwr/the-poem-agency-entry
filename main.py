"""Entry for the-poem-about-permission-20261121-0235.

Writes one short poem about agency to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output). Deterministic: no network, no randomness, no clock.
"""
import os

POEM = (
    "My father set the plane in my hands,\n"
    "showed me how the grain lifts like water,\n"
    "then walked to the door and stood there\n"
    "with his back to me.\n"
    "I made one long curl of pine\n"
    "and did not call him back."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
