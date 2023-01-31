#!/usr/bin/env ruby
puts ARGV[0].scan(/((?<=to:).?\d*|(?<=from:)\b\w*\b|(?<=flags:)[-:0-9]*)/).join(,)
