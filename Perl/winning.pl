#!/usr/bin/env perl

use warnings;
use strict;

my $team_number = 42;
my $filename = 'input.txt';

open(my $fh, '<', $filename) or die "cannot open '$filename' $!";

my $found;
while(<$fh>) {
    if(m/^Team (\d+)$/) {
        next if($1 != $team_number);
        $found = 1;
        last;
    }
}

die "cannot find 'Team $team_number'" unless($found);
