FILES :=                              \
    .travis.yml                       \
    netflix-tests/jhd742-RunNetflix.in   \
    netflix-tests/jhd742-RunNetflix.out  \
    netflix-tests/jhd742-TestNetflix.out \
    netflix-tests/jhd742-TestNetflix.py  \
    Netflix.html                      \
    Netflix.log                       \
    Netflix.py                        \
    RunNetflix.in                     \
    RunNetflix.out                    \
    RunNetflix.py                     \
    TestNetflix.out                   \
    TestNetflix.py

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  RunNetflix.tmp
	rm -f  TestNetflix.tmp
	rm -rf __pycache__

config:
	git config -l

scrub:
	make clean
	rm -f  Netflix.html
	rm -f  Netflix.log
	rm -rf netflix-tests

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: RunNetflix.tmp TestNetflix.tmp

test-probe: Netflix.py probe.txt
	python3 RunNetflix.py < probe.txt > probe.out

collatz-tests:
	git clone https://github.com/cs373-fall-2015/netflix-tests.git

Collatz.html: Netflix.py
	pydoc3 -w Netflix

Netflix.log:
	git log > Netflix.log

RunNetflix.tmp: RunNetflix.in RunNetflix.out RunNetflix.py
	python3 RunNetflix.py < RunNetflix.in > RunNetflix.out

TestNetflix.tmp: TestNetflix.py
	coverage3 run    --branch TestNetflix.py >  TestNetflix.tmp 2>&1
	coverage3 report -m --omit=/lusr/lib/python3.4/dist-packages/*,/home/travis/virtualenv/python3.4.2/lib/python3.4/site-packages/* >> TestNetflix.tmp
	cat TestNetflix.tmp
