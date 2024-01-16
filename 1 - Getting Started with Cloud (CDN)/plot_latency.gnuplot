set datafile separator ","
set xlabel "Request"
set ylabel "Time (seconds)"
set title "Latency Metrics"
plot "latency_metrics.txt" using 1:2 with linespoints title "Total Time", \
     "latency_metrics.txt" using 1:3 with linespoints title "Connection Time", \
     "latency_metrics.txt" using 1:4 with linespoints title "TTFB"
set datafile separator ","
set xlabel "Request"
set ylabel "Time (seconds)"
set title "Latency Metrics"
plot "latency_metrics.txt" using 1:2 with linespoints title "Total Time", \
     "latency_metrics.txt" using 1:3 with linespoints title "Connection Time", \
     "latency_metrics.txt" using 1:4 with linespoints title "TTFB"
