import nintaco.api.*;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Mario {

  private static final String STRING = "Hello, World!";
  
  private static final int SPRITE_ID = 123;
  private static final int SPRITE_SIZE = 32;
  
  private final API api = ApiSource.getAPI();
  
  private int spriteX = 0;
  private int spriteY = 8;
  private int spriteVx = 1;
  private int spriteVy = 1;
  
  private int strWidth;
  private int strX;
  private int strY;

  private List<String> commands;
  
  public void launch()throws Exception {
  	commands = new ArrayList<>();
  	File file = new File("C:/Users/sileob/Downloads/Nintaco_API_2018-09-03/languages/Java/commands.txt");
  	BufferedReader br = new BufferedReader(new FileReader(file));
  	String st;
  	while ((st = br.readLine()) != null){ 
    	commands.add(st);
  	}

    api.addFrameListener(this::renderFinished);
    api.addStatusListener(this::statusChanged);
    api.addActivateListener(this::apiEnabled);
    api.addDeactivateListener(this::apiDisabled);
    api.addStopListener(this::dispose);
    api.run();
  }
  
  private void apiEnabled() {
    System.out.println("API enabled");
  }
  
  private void apiDisabled() {
    System.out.println("API disabled");
  }
  
  private void dispose() {
    System.out.println("API stopped");
  }
  
  private void statusChanged(final String message) {
    System.out.format("Status message: %s%n", message);
  }
  
  private void renderFinished() {
  	if(commands.size() > 0)
  	{
	    String line = commands.remove(0);
	    if(line.contains("jump"))
	    {
	    	api.writeGamepad(0,0,true);
	    }
	    else
	    {
	    	api.writeGamepad(0,0,false);
	    }

	    if(line.contains("run"))
	    {
	    	api.writeGamepad(0,1,true);
	    }
	    else
	    {
	    	api.writeGamepad(0,1,false);
	    }

	    if(line.contains("right"))
	    {
	    	api.writeGamepad(0,7,true);
	    }
	    else
	    {
	    	api.writeGamepad(0,7,false);
	    }
	}
  }
  
  public static void main(final String... args)throws Exception {
    ApiSource.initRemoteAPI("localhost", 9999);
    new Mario().launch();
  }
}