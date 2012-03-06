#!/usr/bin/rdmd

import std.stdio, std.string, std.algorithm;

void main() {
    size_t[string] dictionary;
    foreach (line; stdin.byLine()) {
        // Break sentence into words
        // Add each word in the sentence to the vocabulary
        foreach (word; splitter(strip(line))) {
            if (word in dictionary) continue; // Nothing to do
            auto newID = dictionary.length;
            dictionary[word.idup] = newID;
            writeln(newID, '\t', word);
        }
    }
}
