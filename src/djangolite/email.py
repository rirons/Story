from django.core.mail import send_mail
from django.http import HttpResponse

msg = """
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

<style>

    .pageHeader
    {
        border: none;
        width: 1248px;
    }

    .pageSetup{
        border: 1px solid #BBDDBB;

    }

    .reportHeader
    {
        border: none;
        width: 1400px;
    }

    td{
        overflow: hidden;
        text-overflow: ellipsis;
        word-wrap: break-word;
    }


    h2 {
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
    }


    table {

        margin-left: auto;
        margin-right: auto;
    }
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    th, td {
        padding: 3px;
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 90%;
    }

    thead tr th {
    postion:absolute;
    }
    table tbody tr:hover {
        background-color: #dddddd;
    }
    .wide {
        flex
    }

     .box {
            display: flex;
            flex-wrap: wrap;
          }

    .this {

        font-family: Snell Roundhand, cursive;
        }

    h1 {
    border: 1px solid #BBDDBB;
    }
</style>

</head>

<body>


<a href=https://premiermushrooms.sharepoint.com/:x:/s/FoodSafety/Ee9ayQeWrUNLuNmaziU-ESUBraUXWuCvIzYUgeJjHDl5DQ?e=MTTuXG&download=1 download=https://premiermushrooms.sharepoint.com/:x:/s/FoodSafety/Ee9ayQeWrUNLuNmaziU-ESUBraUXWuCvIzYUgeJjHDl5DQ?e=MTTuXG&download=1>Download as Excel</a>



<script>



   function toggleZoomScreen() {
       document.body.style.zoom = "50%";
   }
</script>



</h1>
</center>

    <h2>  </h2>
<table border="1" class="dataframe table-responsive">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">Lbs</th>
      <th>Total Item</th>
    </tr>
    <tr>
      <th>Ship Date</th>
      <th>02/13/2021</th>
      <th colspan="2" halign="left">02/14/2021</th>
      <th></th>
    </tr>
    <tr>
      <th>Customer:</th>
      <th>Ok Produce</th>
      <th>Allianet, Inc</th>
      <th>Produce Express, Inc</th>
      <th></th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1001-White-Med-10lb</th>
      <td>0</td>
      <td>20</td>
      <td>0</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1001-White-Med-10lb-Sustain</th>
      <td>0</td>
      <td>0</td>
      <td>1000</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>1002-White-Smll-10lb</th>
      <td>0</td>
      <td>0</td>
      <td>200</td>
      <td>200</td>
    </tr>
    <tr>
      <th>1003-White-Open10lb</th>
      <td>0</td>
      <td>0</td>
      <td>200</td>
      <td>200</td>
    </tr>
    <tr>
      <th>2021-RegPort4''-4.5''-5lb</th>
      <td>0</td>
      <td>10</td>
      <td>200</td>
      <td>210</td>
    </tr>
    <tr>
      <th>2043-Brn-Med-10lb</th>
      <td>800</td>
      <td>100</td>
      <td>200</td>
      <td>1100</td>
    </tr>
    <tr>
      <th>5013-1/4''SlOpen-5lb</th>
      <td>0</td>
      <td>0</td>
      <td>400</td>
      <td>400</td>
    </tr>
    <tr>
      <th>8-100-6-WW-12/8oz</th>
      <td>1500</td>
      <td>0</td>
      <td>0</td>
      <td>1500</td>
    </tr>
    <tr>
      <th>8-102-0WS-12/8oz</th>
      <td>1500</td>
      <td>0</td>
      <td>0</td>
      <td>1500</td>
    </tr>
    <tr>
      <th>8-103-7-PrtCap-8/6oz</th>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>60</td>
    </tr>
    <tr>
      <th>8-105-1-BBW-12/8oz</th>
      <td>3000</td>
      <td>0</td>
      <td>0</td>
      <td>3000</td>
    </tr>
    <tr>
      <th>8-106-8-SBB-12/8oz</th>
      <td>3000</td>
      <td>0</td>
      <td>0</td>
      <td>3000</td>
    </tr>
    <tr>
      <th>8-115-PEsmll-1/8''-4/40oz</th>
      <td>0</td>
      <td>0</td>
      <td>600</td>
      <td>600</td>
    </tr>
    <tr>
      <th>Service</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Total Customer</th>
      <td>9860</td>
      <td>130</td>
      <td>2800</td>
      <td>12790</td>
    </tr>
  </tbody>
</table>
</div>
</body>
</html>
"""


def sendSimpleEmail(request):
    emailto = 'rirons@farmersfreshusa.com'
    res = send_mail("hello paul", "how bout that html son", "gshit@guknow.com", [emailto],html_message=msg)
    return HttpResponse('%s'%res)
