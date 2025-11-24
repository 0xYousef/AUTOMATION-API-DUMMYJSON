package automation.api.hooks;

import java.util.HashMap;
import java.util.Map;

import com.automation.api.config.Environment;

import lombok.Builder;
import lombok.NoArgsConstructor;

@NoArgsConstructor
public class TestBais {
    
    private Environment env;
    
    protected String url;

    @Builder
    public TestBais(String url){
        this.url = url;
        this.env = new Environment();
    }
    
    public String url(){
        return url;
    }
    
    public Object getEnvirment(String key){
        return env.get(key);
    }
    
    public Map<String,Object> setEnvirment(String key, Object value){
        env.set(key, value);
        Map<String, Object> result = new HashMap<>();
        result.put(key, value);
        return result;
    }
}