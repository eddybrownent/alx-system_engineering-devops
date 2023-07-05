#!/usr/bin/env ruby
# This script contains a regular expression that matches a
# string that starts with 'h' and ends with 'n' and has any
# single charater in between

puts ARGV[0].scan(/^h\wn/).join
