#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

struct Rule {
    vector<string> needs;
    string adds;
    string reason;
};

int main() {
    cout << "Samarth Mishra | EN24CS3010910\n";
    cout << "Course Adviser Expert System\n";
    cout << "Enter 0/1 for: C++ done, DSA done, databases done,\n"
         << "AI interest, web interest, project time: ";
    const vector<string> input = {
        "cpp", "dsa", "db", "ai_interest", "web_interest", "time"
    };
    set<string> facts;
    for (const auto& key : input) {
        string answer;
        if (!(cin >> answer) || (answer != "0" && answer != "1")) {
            cerr << "Invalid input: each answer must be 0 or 1.\n";
            return 1;
        }
        if (answer == "1") facts.insert(key);
    }
    cout << '\n';
    const vector<Rule> rules = {
        {{"ai_ready", "time"}, "AI Mini Project",
         "AI foundations are ready and project time is available."},
        {{"web_ready", "time"}, "Web Mini Project",
         "Web foundations are ready and project time is available."},
        {{"cpp", "dsa", "ai_interest"}, "ai_ready",
         "C++ and DSA are complete; AI interest is present."},
        {{"cpp", "db", "web_interest"}, "web_ready",
         "C++ and databases are complete; web interest is present."}
    };
    bool changed;
    do {
        changed = false;
        for (const auto& rule : rules) {
            bool ready = all_of(rule.needs.begin(), rule.needs.end(),
                                [&](const string& s) { return facts.count(s) != 0; });
            if (ready && facts.insert(rule.adds).second) {
                cout << "Rule: " << rule.reason << '\n';
                changed = true;
            }
        }
    } while (changed);
    bool recommended = false;
    for (const string& course : {"AI Mini Project"s, "Web Mini Project"s})
        if (facts.count(course)) {
            cout << "Recommendation: " << course << '\n';
            recommended = true;
        }
    if (!recommended)
        cout << "No project match. Review prerequisites or project time.\n";
}
