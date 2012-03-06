#!/usr/bin/rdmd

import std.algorithm, std.conv, std.ascii, std.regex,
    std.range, std.stdio, std.string;

struct PersonData {
    uint totalWordsSpoken;
    uint[string] wordCount;
}

void main() {
    // Accumulates information about dramatis personae
    PersonData[string] info;

    // Fill info
    string currentParagraph;
    foreach (line; stdin.byLine()) {
        if ((line.startsWith("    ")
                && line.length > 4
                && isAlpha(line[4]))) {
            // Persona is continuing a line
            currentParagraph ~= line[3 .. $];
        } else if (line.startsWith("  ")
                && line.length > 2
                && isAlpha(line[2])) {
            // Persona just started speaking
            addParagraph(currentParagraph, info);
            currentParagraph = to!string(line[2 .. $]);
        }
    }

    if (!currentParagraph.empty)
        addParagraph(currentParagraph, info);

    // Done, now print collected information
    printResults(info);
}

void addParagraph(string line, ref PersonData[string] info) {

    // Figure out persona and sentence
    line = strip(line);
    auto sentence = std.algorithm.find(line, ". ");

    if (sentence.empty) {
        return;
    }

    auto persona = line[0 .. $ - sentence.length];
    sentence = toLower(strip(sentence[2 .. $]));

    // Get the words spoken
    auto words = std.regex.split(sentence, regex("[ \t,.;:?]+"));

    // Insert of update information
    if (!(persona in info)) {
        // First time this persona speaketh
        info[persona] = PersonData();
    }

    info[persona].totalWordsSpoken += words.length;
    foreach (word; words) ++info[persona].wordCount[word];
}

void printResults(PersonData[string] info) {
    foreach (persona, data; info) {
        writefln("%20s %6u %6u", persona, data.totalWordsSpoken,
            data.wordCount.length);
    }
}


