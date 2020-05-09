NAME = crypto.py
ARGV = "0123456789"
ALP_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALP_L = "abcdefghijklmnopqrstuvwxyz"

all: test_alp
	python $(NAME) $(ARGV)

test_alp:
	python $(NAME) $(ALP_U)
	python $(NAME) $(ALP_L)
	python $(NAME) $(ALP_U) $(ARGV) $(ALP_L)
