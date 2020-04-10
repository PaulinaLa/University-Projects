
function naturals()
{
    for (var i = 1; i < 100000; i++)
    {
        var sum = 0;
        var copy = i;
        var works = true;
        while (copy)
        {
            sum += copy % 10;
            if (i % (copy % 10))
            {
                works = false;
                break;
            }
            copy  = Math.floor(copy/10);
        }

        if (i % sum === 0 && works)
        {
            console.log(i);
        }
        
    }
}
naturals();