#!/usr/bin/env ruby
# This script has a regular expressio that matches some cases

puts ARGV[0].scan(/hbt{1,4}n/).join
