#include <iostream>
#include <fstream>
#include <string>  
#include <map>   
#include <vector>
#include <assert.h>

// Const to prevent changes, & for passing by referance
std::vector<int> detect_digits(const std::string& text, const std::map<char, int>& digit_dict) {
    std::vector<int> digits; // Declare a vector to store the digits
    for (char ch : text) { // Iterate through each character in the text
        if (digit_dict.find(ch) != digit_dict.end()) { // Check if the character is in the digit map
            digits.push_back(digit_dict.at(ch)); // If it is, add the corresponding digit to the vector
        }
    }
    return digits; // Return the vector of digits
}

int main() {
    std::map<char, int> digit_dict = {{'1', 1}, {'2', 2}, {'3', 3}, {'4', 4}, 
                                      {'5', 5}, {'6', 6}, {'7', 7}, {'8', 8}, {'9', 9}};
    std::ifstream file("example.txt"); 
    std::string line;
    int total = 0; // Initialize total to 0

    while (getline(file, line)) { // Read the file line by line
        auto digit_list = detect_digits(line, digit_dict); 
        if (!digit_list.empty()) {
            total += 10 * digit_list.front() + digit_list.back(); // Add the calculated value to total
        }
    }

    file.close();
    assert(total == 142);

    // The following block of code does the same as above but for "input.txt"
    std::ifstream inputFile("input.txt"); 
    total = 0;

    while (getline(inputFile, line)) {
        auto digit_list = detect_digits(line, digit_dict);
        if (!digit_list.empty()) {
            total += 10 * digit_list.front() + digit_list.back();
        }
    }

    inputFile.close();
    std::cout << "Input total: " << total << std::endl;

    return 0;
}
