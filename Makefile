NAME = crypto.py
ARGV = "0123456789"
ALP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

all: test_alp
	python $(NAME) $(ARGV)

test_alp:
	python $(NAME) $(ALP)
