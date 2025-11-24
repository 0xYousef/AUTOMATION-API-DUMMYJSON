package com.automation.api.config;

import java.util.HashMap;
import java.util.Map;

public class Environment {

    private final Map<String, Object> environment;

    public Environment() {
        this.environment = new HashMap<>();
    }

    public void set(String key, Object value) {
        environment.put(key, value);
    }

    public Object get(String key) {
        return environment.getOrDefault(key, null);
    }

    public boolean contains(String key) {
        return environment.containsKey(key);
    }

    public void clear() {
        environment.clear();
    }

 
}
