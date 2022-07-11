package nz.httpete.fetcher;

public class Main {
    public static void main(String[] args) {
        Fetcher fetcher = new Fetcher("https://faa.gov"); // TODO: load from env-based config
        fetcher.Run();
    }
}