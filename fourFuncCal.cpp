#include <iostream>
#include <string>
#include <stack>
#include <map>
#include <cmath>


using namespace std;

struct Fraction {
    int numerator;
    int denominator;
};

struct Value {
    string name;
    Fraction fraction;
};

class Calculator {
private:
    stack<Value> numStack;
    stack<char> opStack;
    map<string, Fraction> varDict;
    string expression;

    void clearStacks() {
        while (!numStack.empty()) {
            numStack.pop();
        }
        while (!opStack.empty()) {
            opStack.pop();
        }
    }

    void performOp() {
        char op = opStack.top();
        opStack.pop();
        Value right = numStack.top();
        numStack.pop();
        Value left = numStack.top();
        numStack.pop();
        Value result;
        if (op == '=') {
            if (left.name.empty()) {
                cout << "Error: left side of assignment must be a variable" << endl;
                return;
            }
            varDict[left.name] = right.fraction;
            result = right;
        } else {
            if (!left.name.empty()) {
                left.fraction = varDict[left.name];
            }
            if (!right.name.empty()) {
                right.fraction = varDict[right.name];
            }
            result.fraction = calculate(left.fraction, right.fraction, op);
        }
        numStack.push(result);
    }

    Fraction calculate(Fraction left, Fraction right, char op) {
        Fraction result;
        switch (op) {
            case '+':
                result.numerator = left.numerator * right.denominator + right.numerator * left.denominator;
                result.denominator = left.denominator * right.denominator;
                break;
            case '-':
                result.numerator = left.numerator * right.denominator - right.numerator * left.denominator;
                result.denominator = left.denominator * right.denominator;
                break;
            case '*':
                result.numerator = left.numerator * right.numerator;
                result.denominator = left.denominator * right.denominator;
                break;
            case '/':
                result.numerator = left.numerator * right.denominator;
                result.denominator = left.denominator * right.numerator;
                break;
            default:
                cout << "Error: invalid operator" << endl;
                break;
        }
        return result;
    }

    int precedence(char op) {
        switch (op) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '=':
                return 3;
            case '(':
                return 4;
            case '$':
                return 0;
            default:
                cout << "Error: invalid operator" << endl;
                return -1;
        }
    }

    bool isDigit(char c) {
        return c >= '0' && c <= '9';
    }

    bool isLetter(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }

    bool isOperator(char c) {
        return c == '+' || c == '-' || c == '*' || c == '/' || c == '=';
    }

    Fraction convertToFraction(string s) {
        Fraction result;
        int i = 0;
        while (i < s.length() && s[i] != '/') {
            i++;
        }
        if (i == s.length()) {
            result.numerator = stoi(s);
            result.denominator = 1;
        } else {
            result.numerator = stoi(s.substr(0, i));
            result.denominator = stoi(s.substr(i + 1));
        }
        return result;
    }

    void printFraction(Fraction f) {
        if (f.denominator == 1) {
            cout << f.numerator;
        } else {
            cout << f.numerator << "/" << f.denominator;
        }
    }

public:
    Calculator(string expression) {
        this->expression = expression;
    }

    void evaluate() {
        clearStacks();
        opStack.push('$');
        int i = 0;
        while (i < expression.length()) {
            if (expression[i] == ' ') {
                i++;
            } else if (isDigit(expression[i])) {
                string num = "";
                while (i < expression.length() && isDigit(expression[i])) {
                    num += expression[i];
                    i++;
                }
                Value v;
                v.fraction = convertToFraction(num);
                numStack.push(v);
            } else if (isLetter(expression[i])) {
                string name = "";
                while (i < expression.length() && isLetter(expression[i])) {
                    name += expression[i];
                    i++;
                }
                Value v;
                v.name = name;
                numStack.push(v);
            } else if (isOperator(expression[i])) {
                while (precedence(opStack.top()) >= precedence(expression[i])) {
                    performOp();
                }
                opStack.push(expression[i]);
                i++;
            } else {
                cout << "Error: invalid character" << endl;
                return;
            }
        }
        while (opStack.top() != '$') {
            performOp();
        }
        if (numStack.size() == 1) {
            Value result = numStack.top();
            if (!result.name.empty()) {
                result.fraction = varDict[result.name];
            }
            printFraction(result.fraction);
            cout << endl;
        } else {
            cout << "Error: invalid expression" << endl;
        }
    }
};

int main() {
    string expression;
    while (getline(cin, expression)) {
        Calculator calculator(expression);
        calculator.evaluate();
    }
    return 0;
}
