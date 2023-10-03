#!/usr/bin/env ruby
# Matches htbn that starts with h and end with n
puts ARGV[0].scan(/^h.n$/).join
