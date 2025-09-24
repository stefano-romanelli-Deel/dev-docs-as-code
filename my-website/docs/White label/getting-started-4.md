---
title: "Getting Started"
slug: "getting-started-4"
excerpt: ""
hidden: false
createdAt: "Tue Feb 20 2024 13:02:49 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Feb 27 2024 18:26:48 GMT+0000 (Coordinated Universal Time)"
---
## Employee Cost Calculator

### Determine employee costs across the globe with an embeddable UI component.

The Employee Cost Calculator is a UI element created to be used on the web that accepts inputs to calculate the costs to hire a new employee.

## How to use

1. Import the library script from the CDN and add it to the head of your frontend app.

> **Module URL:** `https://white-label-sdk.deel.com/index.js`

```html
<html>
  <head>
    <script type="module" src="../index.js" />
  </head>
  <body />
</html>
```

2. Add a HTML element with an id that you'll use later to setup the calculator.

```html
<html>
  <head>
    <script type="module" src="../index.js" />
  </head>
  <body>
    <div id="employee-calculator-element"></div>
  </body>
</html>
```

3. To use our library you'll need to provide a GET endpoint URL that will communicate with our API to create a new public token, then your endpoint **must** return the token following the format below:

```js
{
  token: 'public-token-from-our-api';
}
```

1. After having your endpoint ready for use on your platform, you can pass the endpoint URL as a parameter for the library instance as the example below illustrates. The second parameter is not required, you should use only when in a need to use demo environment instead of production.

```html
<html>
  <head>
    <script type="module" src="../index.js" />
  </head>
  <body>
    <div id="employee-calculator-element"></div>
    <script type="module">
      const deel = Deel(
        'your endpoint to fetch for a public token',
        'environment you want to use',
      );

      const elements = deel.elements();
      const calculator = elements.create('employee-calculator');

      calculator.mount('employee-calculator-element');
    </script>
  </body>
</html>
```

## Customization

You can customize how the calculator looks like all you want. When using the `elements.create` method you can add a second parameter to add styles to the calculator.

```ts
const calculator = elements.create('employee-calculator', {
  styles: {
    components: {
      container: {
        width: '100%',
        centered: true,
      },
    },
  },
});
```

### Elements

We separate our stylization into two main elements: common variables and components. So when calling the create method the second parameter is used to pass the styles and the keys are `common` for common variables and `components` for all the components used in our UI. The properties that which one of these receive are describe on the sections below.

| Elements   | Description                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------ |
| common     | Common variables that can setup styles for the whole page, as font size, font family and others. |
| components | Group all components that can have its own styles and be customized.                             |

### Common elements

| Element         | Type   | Default Value |
| --------------- | ------ | ------------- |
| fontSizeBase    | string | 14px          |
| fontFamily      | string | sans-serif    |
| primaryColor    | string | # 2c71f0      |
| backgroundColor | string | # f4f3f6      |
| textColor       | string | # 01090f      |

### Components elements

The components umbrella it's a bit more complex since we have nested elements within.

| Element            | Description                                                                                                                   | CSS Properties Supported                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| container          | The highest parent element that embraces the whole calculator.                                                                | width, height, centeredX, centeredY, centered                                                                              |
| content            | The inner wrapper of the calculator that determines the size of the children elements inside.                                 | maxWidth                                                                                                                   |
| select             | The Select field used on the form.                                                                                            | borderRadius, borderColor, activeBorderColor, arrowColor, backgroundColor, fontSize, textColor                             |
| input              | The Input field used on the form.                                                                                             | borderRadius, borderColor, activeBorderColor, color, backgroundColor, fontSize, textColor                                  |
| calculateButton    | The Button that triggers the calculation                                                                                      | borderRadius, color, backgroundColor, fontSize, disabledBackgroundColor, disabledColor, alignment, loaderColor, loaderSize |
| backButton         | The Button to return to the form visualization                                                                                | textColor, fontSize                                                                                                        |
| dataGrid           | The data table that holds the result of the calculation                                                                       | borderColor, borderRadius                                                                                                  |
| dataGridRow        | The row of the data table with the calculation results                                                                        | borderColor                                                                                                                |
| dataGridCell       | The cell of the data table with the calculation results                                                                       | borderColor, backgroundColor, textColor, fontSize                                                                          |
| dataGridCellColumn | The column cell of the data table with the calculation results                                                                | fontWeight, textColor, fontSize                                                                                            |
| dataGridRowExtra   | The highlighted row of the data table with the calculation results                                                            | backgroundColor                                                                                                            |
| dataGridRowHeader  | The header row of the data table with the calculation results                                                                 | backgroundColor, textColor                                                                                                 |
| additionalNotes    | Additional notes that are displayed at bottom below the data grid with extra information about hiring on the selected country | fontSize, textColor, lineHeight                                                                                            |
| loader             | The loader displayed inside while loading data                                                                                | backgroundColor, size                                                                                                      |
| headerTitle        | The title that appears on the first screen                                                                                    | textColor, fontSize, fontFamily, fontWeight                                                                                |
| errorMessage       | The popup that it's displayed when an API error occur                                                                         | textColor, fontSize, borderRadius, backgroundColor                                                                         |

## How to get a public token

To seamlessly integrate our embeddable UI into your application, we require you to create and provide an endpoint that facilitates the retrieval of a public token. This token is essential for securely accessing and utilizing our UI components within your application environment.

You'll need first to generate a PAT (Personal Access Token) in our platform, follow [this tutorial](https://developer.deel.com/docs/api-tokens-1) on how to do it. To use our library you'll need to select the **Public Token** scope.

### Code example

```ts
import express from 'express';
import cors from 'cors';

app.use(cors());

app.get('/public-token', async (request, response) => {
  const options = {
    method: 'POST',
    headers: {
      accept: 'application/json',
      'content-type': 'application/json',
      authorization: 'Bearer {{here goes the PAT you generated earlier}}',
    },
    body: JSON.stringify({ data: { scope: 'contracts:read' } }),
  };

  const res = await fetch(
    'https://api.letsdeel.com/rest/v2/public-tokens',
    options,
  );
  const data = await res.json();

  return response.json({
    token: data.token,
  });
});
```
