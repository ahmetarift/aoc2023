#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <assert.h>

std::vector<int> detect_digits(const std::string& text,
                               const std::map<char, int>& digit_dict,
                               const std::map<std::string, int>& string_digit_dict) {
    std::vector<int> digits;
    int N = text.size();
    int i = 0;
    while (i < N) {
        if (digit_dict.find(text[i]) != digit_dict.end()) { // if text[i] in digit_dict returns 1, otherwise end
            digits.push_back(digit_dict.at(text[i])); // push_back works like append
            i += 1;
        } else {
            bool found = false;
            for (int len = 3; len <= 5; len++) {
                if (i + len <= N && string_digit_dict.find(text.substr(i, len)) != string_digit_dict.end()) {
                    digits.push_back(string_digit_dict.at(text.substr(i, len))); // substr that starts at i, length is len
                    i += 1;
                    found = true;
                    break;
                }
            }
            if (!found) {
                i += 1;
            }
        }
    }
    return digits;
}

int main() {
    std::map<char, int> digit_dict = {{'1', 1}, {'2', 2}, {'3', 3}, {'4', 4},
                                      {'5', 5}, {'6', 6}, {'7', 7}, {'8', 8}, {'9', 9}};
    std::map<std::string, int> string_digit_dict = {{"one", 1}, {"two", 2}, {"three", 3},
                                                    {"four", 4}, {"five", 5}, {"six", 6},
                                                    {"seven", 7}, {"eight", 8}, {"nine", 9}};

    std::ifstream file("example2.txt");
    std::string line;
    int total = 0;

    while (getline(file, line)) {
        auto digit_list = detect_digits(line, digit_dict, string_digit_dict);
        if (!digit_list.empty()) {
            total += 10 * digit_list.front() + digit_list.back();
        }
    }

    file.close();
    assert(total == 281);

    std::ifstream inputFile("input.txt");
    total = 0;

    while (getline(inputFile, line)) {
        auto digit_list = detect_digits(line, digit_dict, string_digit_dict);
        if (!digit_list.empty()) {
            total += 10 * digit_list.front() + digit_list.back();
        }
    }

    inputFile.close();
    std::cout << "Input total: " << total << std::endl;

    return 0;
}
