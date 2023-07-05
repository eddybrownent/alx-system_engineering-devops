#!/usr/bin/env ruby
# This Regulae expression help us to capture
# SENDER, RECEIVER, FLAGS from a text app messages

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(",")
