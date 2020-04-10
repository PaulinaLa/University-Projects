
function primes ()
{
    console.log (2);
    for (var i = 2; i<10000; i++)
    {   
        for (var j=2; j <Math.sqrt(i); j++)
        {
            var works = true;
            if (i % j == 0){
                works = false;
                break;
            }
        }
        if (works)
        {
            console.log(i);
        }
    }
}

primes()