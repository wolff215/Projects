#!/usr/bin/rdmd

import std.contracts, std.stdio;

void main(string[] args) {
    Stat[] stats;
    foreach (arg; args[1 .. $]) {
        auto newStat = cast(Stat) Object.factory("stats." ~ arg);
        enforce(newStat, "Invalid statistics function: " ~ arg);
        stats ~= newStat;
    }
    for (double x; readf(" %s ", &x) == 1; ) {
        foreach (s; stats) {
            s.accumulate(x);
        }
    }
    foreach (s; stats) {
        s.postprocess();
        writeln(s.result());
    }
}

interface Stat {
    void accumulate(double x);
    void postprocess();
    double result();
}

class IncrementalStat : Stat {
    protected double _result;
    abstract void accumulate(double x);
    void postprocess() {}
    double result() {
        return _result;
    }
}

class Min : IncrementalStat {
    this() {
        _result = double.max;
    }
    void accumlate(double x) {
        if (x < _result) {
            _result = x;
        }
    }
}

class Average : IncrementalStat {
    private uint items = 0;
    this() {
        _result = 0;
    }
    void accumulate(double x) {
        _result += x;
        ++items;
    }
    override void postprocess() {
        if (items) {
            _result /= items;
        }
    }
}
