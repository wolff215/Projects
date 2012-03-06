#!/usr/bin/rdmd

/*
    Compute heights in centimeters for a range of heights
    expressed in feet and inches
*/

import std.stdio;

void main() {
    // Values unlikely to change soon
    immutable inchesPerFoot = 12;
    immutable cmPerInch = 2.54;

    // Loo'n write
    foreach (feet; 5 .. 7) {
        foreach (inches; 0 .. inchesPerFoot) {
            writeln(feet, "'", inches, "''\t",
                (feet * inchesPerFoot + inches) * cmPerInch, " cm");
        }
    }
}
