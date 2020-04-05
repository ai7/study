package hfdp.c01.Strategy;

import org.junit.Test;

public class MiniDuckSimulator {

    @Test
    public void test_MallardDuck() {
        Duck mallard = new MallardDuck();
        mallard.performQuack();
        mallard.performFly();;
    }

    @Test
    public void test_ModelDuck() {
        Duck model = new ModelDuck();
        model.performFly();
        model.setFlyBehavior(new FlyRocketPowered());
        model.performFly();
    }
}
