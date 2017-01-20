In order to limit the number of emails Margaret sends out, the CSS has passed a bill which imposes a per-key-pressed cost on sending out mass emails.  The rate for sending out a mass email is 1 cent per key pressed while writing the body of the email.  Margaret sends out her mass emails from a Nokia flip phone with the following keypad:

<br /><br />

<table class="table" border="1" align="center">
<tr>
<td>1<br>abc</td>
<td>2<br>def</td>
<td>3<br>ghi</td>
</tr>
<tr>
<td>4<br>jkl</td>
<td>5<br>mno</td>
<td>6<br>pqr</td>
</tr>
<tr>
<td>7<br>stu</td>
<td>8<br>vwx</td>
<td>9<br>yz</td>
</tr>
<tr>
<td> </td>
<td>0<br>.,!</td>
<td>#<br>_</td>
</tr>
</table>
<i>* Note that in this case the "_" under the # key is a space</i>
<br /><br />
In order to send the message "hi", Margaret needs to press the "3" key twice, followed by the "3" key 3 more times.  Consequently, the CSS would charge Margaret 5 cents to send out an email containing the text "hi".  Given a message, determine how much the CSS should charge Margaret.
<br />
<h3>Input Format</h3>
<ul>
  <li>A string <code>s</code> representing the message that Margaret wishes to send.  A message will contain only valid characters as defined by the keypad above, and all letters will be lower case.</li>
</ul>

<h3>Output Format</h3>
<ul>
  <li>The amount, in cents, that the CSS should charge Margaret to send the message</li>
</ul>


   <h3>Sample Input</h3>
 <pre>the first ever css contest will be sick nasty kids!</pre>

  <h3>Sample Output</h3>
        <pre>96</pre>
