#!/usr/bin/env ruby
# script output - sender, receiver and flag
puts ARGV[0].scan(/\[from:(\+?\w+)] \[to:(\+?\w+)] \[flags:([-:\d]+)\]/).join(",")
