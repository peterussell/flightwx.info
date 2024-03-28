package info.flightwx.fetcher.infrastructure.config;

import io.github.cdimascio.dotenv.Dotenv;

public class Config {
    private static final Config instance = new Config();
    private Dotenv env;

    public static Config GetConfig() {
        return instance;
    }

    public Config() {
        this.env = Dotenv.configure().directory("./").ignoreIfMissing().load();
    }

    public String get(String variable) {
        return env.get(variable);
    }
}
