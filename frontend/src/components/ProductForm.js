// src/components/ProductForm.js
import React, { useState } from "react";
import axios from "axios";

const ProductForm = () => {
  const [product, setProduct] = useState({
    ProductName: "",
    ProductCode: "",
    variants: [{ name: "", sub_variants: [{ name: "", stock: 0 }] }],
  });

  const handleChange = (e) => {
    setProduct({
      ...product,
      [e.target.name]: e.target.value,
    });
  };

  const handleVariantChange = (index, e) => {
    const newVariants = [...product.variants];
    newVariants[index][e.target.name] = e.target.value;
    setProduct({ ...product, variants: newVariants });
  };

  const handleSubVariantChange = (variantIndex, subVariantIndex, e) => {
    const newVariants = [...product.variants];
    newVariants[variantIndex].sub_variants[subVariantIndex][e.target.name] =
      e.target.value;
    setProduct({ ...product, variants: newVariants });
  };

  const addVariant = () => {
    setProduct({
      ...product,
      variants: [
        ...product.variants,
        { name: "", sub_variants: [{ name: "", stock: 0 }] },
      ],
    });
  };

  const addSubVariant = (index) => {
    const newVariants = [...product.variants];
    newVariants[index].sub_variants.push({ name: "", stock: 0 });
    setProduct({ ...product, variants: newVariants });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/api/products/",
        product
      );
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Product Name</label>
        <input
          type="text"
          name="ProductName"
          value={product.ProductName}
          onChange={handleChange}
        />
      </div>
      <div>
        <label>Product Code</label>
        <input
          type="text"
          name="ProductCode"
          value={product.ProductCode}
          onChange={handleChange}
        />
      </div>
      {product.variants.map((variant, variantIndex) => (
        <div key={variantIndex}>
          <label>Variant Name</label>
          <input
            type="text"
            name="name"
            value={variant.name}
            onChange={(e) => handleVariantChange(variantIndex, e)}
          />
          {variant.sub_variants.map((subVariant, subVariantIndex) => (
            <div key={subVariantIndex}>
              <label>Sub-Variant Name</label>
              <input
                type="text"
                name="name"
                value={subVariant.name}
                onChange={(e) =>
                  handleSubVariantChange(variantIndex, subVariantIndex, e)
                }
              />
              <label>Stock</label>
              <input
                type="number"
                name="stock"
                value={subVariant.stock}
                onChange={(e) =>
                  handleSubVariantChange(variantIndex, subVariantIndex, e)
                }
              />
            </div>
          ))}
          <button type="button" onClick={() => addSubVariant(variantIndex)}>
            Add Sub-Variant
          </button>
        </div>
      ))}
      <button type="button" onClick={addVariant}>
        Add Variant
      </button>
      <button type="submit">Submit</button>
    </form>
  );
};

export default ProductForm;
