NAME = crypto.py
ARGV = "0123456789"
ALP_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALP_L = "abcdefghijklmnopqrstuvwxyz"
TEXT_1 = "On branch master"
TEXT_10 = "Po csbodi nbtufs"
TEXT_2 = "Good Morning, ROT13!"
TEXT_20 = "Tbbq Zbeavat, EBG46!"
TEXT_3 = "Hello. JoJo."
TEXT_30 = "Fcjjm. HmHm."

all: test_alp test_num test_words

test_num:
	python $(NAME) $(ARGV) enc 0
	python $(NAME) $(ARGV) enc 1
	python $(NAME) $(ARGV) enc 2
	python $(NAME) $(ARGV) dec 0
	python $(NAME) $(ARGV) dec 1
	python $(NAME) $(ARGV) dec 2

test_alp:
	python $(NAME) $(ALP_U) enc 0
	python $(NAME) $(ALP_U) enc 1
	python $(NAME) $(ALP_U) enc 2
	python $(NAME) $(ALP_U) dec 0
	python $(NAME) $(ALP_U) dec 1
	python $(NAME) $(ALP_U) dec 2
	python $(NAME) $(ALP_L) enc 0
	python $(NAME) $(ALP_L) enc 1
	python $(NAME) $(ALP_L) enc 2
	python $(NAME) $(ALP_L) dec 0
	python $(NAME) $(ALP_L) dec 1
	python $(NAME) $(ALP_L) dec 2

test_words:
	python $(NAME) $(TEXT_1) enc 0
	python $(NAME) $(TEXT_10) dec 0
	python $(NAME) $(TEXT_2) enc 1
	python $(NAME) $(TEXT_20) dec 1
	python $(NAME) $(TEXT_3) enc 2
	python $(NAME) $(TEXT_30) dec 2
