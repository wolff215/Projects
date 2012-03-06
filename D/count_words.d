#!/usr/bin/rdmd

import std.stdio, std.string, std.algorithm;

void main() {
    // Compute counts
    uint[string] freqs;
    foreach (line; stdin.byLine()) {
        foreach (word; split(strip(line))) {
            ++freqs[word.idup];
        }
    }

    // Print counts
    string[] words = freqs.keys;
    sort!((a, b) { return freqs[a] > freqs[b]; })(words);
    foreach (word; words) {
        writefln("%6u\t%s", freqs[word], word);
    }
}
