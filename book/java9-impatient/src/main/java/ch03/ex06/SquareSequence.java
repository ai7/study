package ch03.ex06;

import java.math.BigInteger;

public class SquareSequence implements Sequence<BigInteger> {

    // make index BigInteger so it'll grow forever
    private BigInteger i = BigInteger.valueOf(0);

    @Override
    public BigInteger next() {
        i = i.add(BigInteger.valueOf(1));
        return i.multiply(i);
    }
}
