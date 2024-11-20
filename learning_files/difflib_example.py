from difflib import SequenceMatcher

s = SequenceMatcher(
    lambda x: x == " ",
    "private Thread currentThread;",
    "private volatile Thread currentThread;",
)
print(round(s.ratio(), 3))

for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)
