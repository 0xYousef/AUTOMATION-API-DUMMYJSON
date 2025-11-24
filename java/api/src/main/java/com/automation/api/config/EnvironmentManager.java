package com.automation.api.config;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class EnvironmentManager {

    private final Properties props = new Properties();
    private final String envName;

    public EnvironmentManager(String envName) {
        this.envName = envName.toLowerCase();
        String fileName = "config/" + this.envName + ".properties";

        try (InputStream input = EnvironmentManager.class
                .getClassLoader()
                .getResourceAsStream(fileName)) {

            if (input == null) {
                throw new RuntimeException("File not found in resources: " + fileName);
            }

            props.load(input);

        } catch (IOException e) {
            throw new RuntimeException("Failed loading: " + fileName, e);
        }
    }

    public String getProperty(String key) {
        return props.getProperty(key);
    }

    public String getRoot() {
        return props.getProperty("root");
    }
}
