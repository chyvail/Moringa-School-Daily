export default function BlogItem({src,category,title,description,authorIcon,authorName}){
    return (
        <div className="card bg-light text-dark mb-3 d-inline-block my-3 mx-3 px-2 py-2 " style={{ width: '18rem' }}>
          <img src={src} style={{height:"200px", width:"360px"}} className="card-img-top" alt="..." />
          <div className="card- body">
            <h5 className="card-category">{category}</h5>
            <h5 className="card-title">{title.slice(0-50)}</h5>
            <p className="card-description">{description?description.slice(0,90):"custom description"}</p>
            <div className="d-flex align-items-center">
              <img src={authorIcon} className="author-icon" alt="Author Icon" />
              <span className="author-name">{authorName}</span>
            </div>
          </div>
        </div>
      );
    }