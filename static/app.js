function calculate()
{
    let op1 = document.getElementById('op1').value;
    let op2 = document.getElementById('op2').value;
    let op = document.getElementById('op').value;

    var ans;

    let root = document.getElementById('result');
        while (root.firstChild) {
            root.removeChild(root.firstChild);
        }
    
    if(op=="+")
    ans=Number(op1)+Number(op2);
    else if(op=="-")
    ans=Number(op1)-Number(op2);
    else if(op=="*")
    ans=Number(op1)*Number(op2);
    else if(op=="/")
    ans=Number(op1)/Number(op2);
    else if(op=="<")
    ans=Number(op1)<Number(op2);
    else if(op==">")
    ans=Number(op1)>Number(op2);
    else if(op=="<=")
    ans=Number(op1)<=Number(op2);
    else if(op==">=")
    ans=Number(op1)>=Number(op2);
    else if(op=="==")
    ans=Number(op1)==Number(op2);
    else if(op=="|")
    ans=Number(op1)|Number(op2);
    else if(op=="&")
    ans=Number(op1)&Number(op2);
    else if(op=="^")
    ans=Number(op1)^Number(op2);
    else if(op=="%")
    ans=Number(op1)%Number(op2);
    else if(op=="~")
    ans=~Number(op1);
    let ul = document.getElementById('result');
    let p1 = document.createElement('p');
    p1.innerHTML = (`<p><strong>Result:</strong>${ans}</p>`)
    ul.appendChild(p1);

    let url='/senddata';

    let data={'op1':op1,'op2':op2,'op':op,'ans':ans};

    $.post(url,data);
}