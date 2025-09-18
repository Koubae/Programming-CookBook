import "runtime"

func main() {
    runtime.GOMAXPROCS(runtime.NumCPU()) // use all CPU cores
}
