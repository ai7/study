package ch02;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;
import org.junit.Before;
import org.junit.Test;

public class Ex09Test {

    Exercise09.Car myvolt = new Exercise09.Car(37, 9.3);

    @Test
    public void test_AddGas() {
        // act
        myvolt.addGas(3.5);
        myvolt.addGas(5.7);
        // verify
        assertThat(myvolt.getFuel(), is(9.2));
    }

    @Test
    public void test_AddGasMax() {
        // act
        myvolt.addGas(10);
        // verify
        assertThat(myvolt.getFuel(), is(9.3));
    }

    public void test_travel() {
        // arrange
        myvolt.addGas(5);
        // act
        myvolt.travelMiles(150);
        // verify
        assertThat(myvolt.getDistance(), is(150));
        assertThat(myvolt.getFuel(), is(150/37.0));
    }

    @Test
    public void test_travelRange() {
        // arrange
        myvolt.addGas(5);
        // act
        myvolt.travelMiles(200);
        // verify
        assertThat(myvolt.getDistance(), is(5.0*37));
        assertThat(myvolt.getFuel(), is(0.0));
    }

}
