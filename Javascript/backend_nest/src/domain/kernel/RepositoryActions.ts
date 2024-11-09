export interface Add<T> {
  add(entity: T): Promise<T>;
}

export interface FindOne<T> {
  findOne(id: number): Promise<T | null>;
}

export interface FindMany<T> {
  findMany(): Promise<T[]>;
}

export interface Update<T> {
  update(id: number, entity: T): Promise<T | null>;
}

export interface Delete {
  delete(id: number): Promise<boolean>;
}

export interface CrudRepository<T> extends Add<T>, FindOne<T>, FindMany<T>, Update<T>, Delete {}
