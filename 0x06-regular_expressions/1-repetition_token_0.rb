#!/usr/bin/env ruby
# This script has a regular expression that matches some cases

puts ARGV[0].scan(/hbt{2,5}n/).join
