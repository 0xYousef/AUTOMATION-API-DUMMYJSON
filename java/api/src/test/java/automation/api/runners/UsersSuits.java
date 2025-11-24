package automation.api.runners;

import com.automation.api.config.EnvironmentManager;

import automation.api.hooks.TestBais;

public class UsersSuits extends TestBais {

    public UsersSuits(EnvironmentManager env){
        super(env.getRoot());
    }


}
