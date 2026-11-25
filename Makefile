CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -Werror
TARGET := exp12

all: $(TARGET)

$(TARGET): exp12.cpp
	$(CXX) $(CXXFLAGS) exp12.cpp -o $(TARGET)

test: $(TARGET)
	python tests/verify.py

clean:
	rm -f exp12 exp12.exe
